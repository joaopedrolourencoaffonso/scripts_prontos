#fonte:  https://platform.openai.com/docs/quickstart?context=python

from openai import OpenAI

client = OpenAI(
    api_key='SUA CHAVE DA API AQUI'
)

prompt = """ Style: 'Doodle'. A aerial view of a little tropical island with a tower and small phishing village. Warmth colors. Is a small, happy and proud place.
#castle #castledrawing #cartoonsforadults"""

response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(image_url)

# Algumas ideias de prompt
prompt = """ Style: 'Doodle'. A castle in the top a mountain. The castle has for wall with for towers with conical roofs. The castle is in a narrow mountain with red trees. Smoke cames out of one of the towers.
#castle #castledrawing #cartoonsforadults"""

prompt = """ Style: 'Doodle'. An island. In an corner a big totalitarian fortress with a great tower. In the other, several shacks and poor houses. Also a small coleseum. It's a sad place with tones of brown and grey but also red flowers to give some warmth.
#castle #castledrawing #cartoonsforadults"""

prompt = """ Style: 'Doodle'. An elf with red skin, leather armor and a rapier in his belt. He is a swashbuckling hero walking among a florest of trees with yellow trunks and blue leafs. 
#characterdesign #drawing #cartoonsforadults"""

prompt = """ Style: 'Doodle'. A little phishing vilage in the coast, a seamonster can be seen in the waters.
#castle #castledrawing #illustration"""
