#!/usr/bin/env python3
import click
import os
from .config import Config
from .ai_client import AIClient
from .command_executor import CommandExecutor

@click.group()
def cli():
    """Easy-grep: Natural language to command line converter"""
    pass

@cli.command()
@click.argument('query', nargs=-1)
def ask(query):
    """Convert natural language to command line commands"""
    query_text = ' '.join(query)
    
    config = Config()
    if not config.is_configured():
        api_key = click.prompt('Please enter your Anthropic API key', hide_input=True)
        config.save_api_key(api_key)
        click.echo('Configuration saved successfully!')
        
    ai_client = AIClient(config.get_api_key())
    command = ai_client.generate_command(query_text)
    
    click.echo(f"\nGenerated command: {command}")
    
    if click.confirm('Do you want to execute this command?'):
        executor = CommandExecutor()
        result = executor.execute(command)
        click.echo(result)
    else:
        click.echo('Command execution cancelled.')

if __name__ == '__main__':
    cli() 