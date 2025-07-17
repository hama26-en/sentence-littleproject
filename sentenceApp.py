Start
Repeat
    Display "Enter a sentence that starts with a word and ends with a period:"
    Read sentence
Until sentence does not start with a space AND sentence ends with '.'

Set char_count to 0
Set word_count to 1
Set vowel_count to 0

For each character char in sentence do
    Increment char_count by 1

    If char is a space then
        Increment word_count by 1

    If lowercase(char) is in ['a', 'e', 'i', 'o', 'u'] and uppercase(char) is in ['A','E','I','O','U'] then
        Increment vowel_count by 1

End For

Display "Character count: ", char_count
Display "Word count: ", word_count
Display "Vowel count: ", vowel_count

End
