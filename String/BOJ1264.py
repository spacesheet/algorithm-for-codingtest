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
  my_input_list = []
  while True:
      my_input_sentence = input().upper()
      if my_input_sentence != '#':
          my_input_list.append(my_input_sentence)
      else:
          break
  my_result_list = sentence_list_vowl_counter(my_input_list)
  for i in my_result_list:
      print(i)

main()