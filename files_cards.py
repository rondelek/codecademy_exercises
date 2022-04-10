from contextlib import contextmanager

@contextmanager
def generic(card_type, sender, receiver):
  card_file = open(card_type, 'r')
  order = open(f'{sender}_generic.txt','w')

  try:
    order.write(f'Dear {receiver}, \n')
    order.write(card_file.read())
    order.write(f'\nSincerely, {sender} \n')
    yield order

  finally:
    card_file.close()
    order.close()

with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as order_1:
  print('Card Generated!')

with open('Mwenda_generic.txt', 'r') as order_1_read:
  print(order_1_read.read())
  

class Personalized:
  
  def __init__(self, sender, receiver):
    self.sender = sender
    self.receiver = receiver
    self.file = open(f'{self.sender}_personalized.txt', 'w')

  def __enter__(self):
    self.file.write(f'Dear {self.receiver} \n')
    return self.file
  
  def __exit__(self, exc_type, exc_value, Traceback):
    self.file.write(f'\n Sincerely, {self.sender}. \n')
    self.file.close()

with Personalized('John', 'Michael') as order_2:
  order_2.write('I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.')

with open('John_personalized.txt', 'r') as order_2_read:
  print(order_2_read.read())

with generic('happy_bday.txt', 'Josiah', 'Remy') as Josiah_generic:
  print('Card for Remy generated, Josiah!')

with Personalized('Josiah', 'Esther') as Josiah_personalized:
  Josiah_personalized.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")
