vowel_list = ['A', 'I', 'O', 'U', 'E']

def sentence_list_vowl_counter(input_list: list) -> list:
    result_list = []
    for sentence in input_list:
        result = 0
        for letter in sentence:
            if letter in vowel_list:
                result += 1
        result_list.append(result)
    return result_list

def main():
  input_list = []
  while True:
      input_sentence = input().upper()
      if input_sentence != '#':
          input_list.append(input_sentence)
      else:
          break
  result_list = sentence_list_vowl_counter(input_list)
  for i in result_list:
      print(i)

main()