import codecs
def delete_html_tags(html_file = 'draft.html', result_file='cleaned.txt'):
      with (codecs.open(html_file, 'r', 'utf-8') as file):
          html = file.read()
          result = []
          inside_tag = False

          for char in html:
              if char == '<':  # Начало тега
                  inside_tag = True
              elif char == '>':  # Конец тега
                  inside_tag = False
              elif not inside_tag:  # Если мы не внутри тега, добавляем символ в результат
                  result.append(char)
          result = ''.join(result).split('\n')
          result = [x.strip() for x in result if x.strip()]
          result = '\n'.join(result)

      with open(result_file, 'w', encoding='utf-8') as output_file:
          output_file.write(result)
      return result

print(delete_html_tags())
