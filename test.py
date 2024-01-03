import cohere
co = cohere.Client('qDLLn4ntg1Lj1KnyuiBq5Rf3WjcdYmEWhtSi7f3H') # This is your trial API key
"""response = co.chat( 
  model='command',
  message='<YOUR MESSAGE HERE>',
  temperature=0.3,
  chat_history=[],
  prompt_truncation='AUTO',
  stream=True,
  citation_quality='accurate',
  connectors=[{"id":"web-search"}],
  documents=[]
)"""
message = "Write a leave apllication letter to boss"
response = co.chat(
	message, 
	model="command", 
	temperature=0.9
)

answer = response.text
print(answer)