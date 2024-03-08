{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "809c16b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import re\n",
    "from collections import Counter\n",
    "\n",
    "def get_text(url):\n",
    "    response = requests.get(url)\n",
    "    soup = BeautifulSoup(response.text, 'html.parser')\n",
    "    # mw-parser-output to klasa HTML uzywana na platformie MediaWiki - jest glownym kontenerem dla tresci\n",
    "    content = soup.find('div', class_='mw-parser-output').text\n",
    "    return content\n",
    "\n",
    "def process_text(text):\n",
    "    #Dopisz kod spelniajacy Punkt 2\n",
    "    #Przekształć tekst do małych liter (lowercase).\n",
    "    text = text.lower()\n",
    "    \n",
    "    #Usuń znaki specjalne oraz interpunkcję.\n",
    "    text = re.sub(r'[^a-zA-Z\\s]', '', text)\n",
    "    \n",
    "    return text\n",
    "\n",
    "def get_ranked_words(text):\n",
    "    ranked_words = None\n",
    "    #Dopisz kod spelniajacy Punkt 3\n",
    "    \n",
    "    #     Podziel tekst na słowa.\n",
    "    words = text.split()\n",
    "\n",
    "    # Zlicz ilość wystąpień dla każdego słowa.\n",
    "    # Znajdź 100 najpopularniejszych w tekście słów.\n",
    "    word_counts = Counter(words)\n",
    "    ranked_words = word_counts.most_common(100)\n",
    "\n",
    "    return ranked_words\n",
    "\n",
    "def write_results(results, filename):\n",
    "    with open(filename, 'w') as file:\n",
    "    #Dopisz kod spelniajacy Punkt 4\n",
    "        for i, (word, count) in enumerate(results, 1):\n",
    "            file.write(f\"{i};{word};{count}\\n\")\n",
    "        pass\n",
    "\n",
    "def main():\n",
    "    url = 'https://en.wikipedia.org/wiki/Web_scraping'\n",
    "    text = get_text(url)\n",
    "    cleaned_text = process_text(text)\n",
    "    final_words = get_ranked_words(cleaned_text)\n",
    "    write_results(final_words, 'output.txt')\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
