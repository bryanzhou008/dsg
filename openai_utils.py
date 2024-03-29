
import time
import openai

def openai_setup(key_path='/local1/bryanzhou008/ecole/keys/_OAI_KEY.txt'):
	with open(key_path) as f:
		key = f.read().strip()

	print("Read key from", key_path)
	openai.api_key = key

def openai_completion(
	prompt,
	#   model="gpt-3.5-turbo-0613",
	model='gpt-3.5-turbo-16k-0613',
	temperature=0,
	return_response=False,
	max_tokens=500,
	):

	# resp = openai.ChatCompletion.create(
	# 		model=model,
	# 		messages=[{"role": "user", "content": prompt}],
	# 		temperature=temperature,
	# 		max_tokens=max_tokens,
	# 	)
	
	resp = openai.chat.completions.create(
			model=model,
			messages=[{"role": "user", "content": prompt}],
   			temperature=temperature,
			max_tokens=max_tokens,
		)
	
	if return_response:
		return resp

	return resp.choices[0].message.content