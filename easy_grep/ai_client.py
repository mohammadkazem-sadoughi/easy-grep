from anthropic import Anthropic

class AIClient:
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)

    def generate_command(self, query):
        """Generate command from natural language query"""
        prompt = f"""
        Convert the following natural language query to a Unix/Linux command.
        Only return the command itself, no explanations.
        Query: {query}
        """
        
        message = self.client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=100,
            temperature=0,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        return message.content.strip() 