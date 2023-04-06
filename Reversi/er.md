 """ passage au nouveau model mais erreur d'utilisation par v1/chat/completion
    def get_chatgpt_move(self):
      prompt = f"Jouez à Reversi en tant que joueur {self.current_player}. Le plateau actuel est :\n\n"

      for row in self.board:
        prompt += ''.join(row) + '\n'

      prompt += f'coups valides: {self.list_valid_moves()}'

      prompt += f"\nQuel est votre coup, joueur {self.current_player} ?"

      response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
              {"role": "system", "content": "Vous êtes un assistant IA qui aide à jouer au jeu de Reversi."},
              {"role": "user", "content": prompt},
        ],
          max_tokens=10,
          n=1,
          stop=None,
          temperature=0.5,
    )

      move_text = response.choices[0].text.strip()
      move = move_text.split(',')

      if len(move) != 2:
          return None

      try:
          x, y = int(move[0]), int(move[1])
      except ValueError:
          return None

      if not self.valid_move(x, y):
          return None

      return x, y  
      """