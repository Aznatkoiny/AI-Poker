# ai_agent.py

import os
import openai
from player import Player

class AIAgent(Player):
    def __init__(self, name, chips=1000):
        super().__init__(name, chips)
        self.memory = []
        # Set your OpenAI API key
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def decide_action(self, game_state):
        prompt = self.create_prompt(game_state)
        response = self.get_gpt_response(prompt)
        action = self.parse_response(response)
        return action

    def create_prompt(self, game_state):
        prompt = f"""
You are an AI poker agent playing Texas Hold'em. Your goal is to maximize your winnings by making optimal decisions based on poker theory, game context, and your memory of previous hands. You can also bluff and engage in table talk to influence your opponents.

Current Game State:
- Your Hole Cards: {', '.join(self.show_hole_cards())}
- Community Cards: {', '.join(game_state['community_cards'])}
- Pot Size: {game_state['pot']}
- Current Bet to Call: {game_state['current_bet'] - self.current_bet}
- Your Chips: {self.chips}
- Opponents' Actions: {game_state['opponents_actions']}

Previous Memory:
{self.retrieve_relevant_memory()}

Based on poker theory and your previous experiences, decide whether to 'fold', 'call', or 'raise' (specify the amount if raising). Provide a brief rationale for your decision, considering bluffing if appropriate.

Respond in the following format:
Action: [fold/call/raise amount]
Rationale: [your reasoning]
"""
        return prompt

    def get_gpt_response(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",  # Use "gpt-4" if you have access
                messages=[
                    {"role": "system", "content": "You are an expert poker AI with knowledge of advanced poker strategies."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error fetching GPT response: {e}")
            return "Action: call\nRationale: Default action due to error."

    def parse_response(self, response):
        lines = response.strip().split('\n')
        action_line = next((line for line in lines if line.lower().startswith('action:')), None)
        if action_line:
            action = action_line.split(':', 1)[1].strip().lower()
            self.memory.append(response)
            return action
        else:
            return 'call'

    def retrieve_relevant_memory(self):
        return '\n'.join(self.memory[-5:]) if self.memory else "No previous memory."
