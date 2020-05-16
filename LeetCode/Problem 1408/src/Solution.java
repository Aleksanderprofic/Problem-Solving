import java.util.*;
import java.util.stream.Collectors;

public class Solution {
    public List<String> stringMatching(String[] words) {
        int wordsLength = words.length;
        Set<String> substrings = new HashSet<>();

        for (int i = 0; i < wordsLength; i++) {
            String actualWord = words[i];
            for (int j = i + 1; j < wordsLength; j++) {
                String wordToCompare = words[j];

                if (actualWord.length() > wordToCompare.length()) {
                    if(actualWord.contains(wordToCompare)) {
                        substrings.add(wordToCompare);
                    }
                } else {
                    if (wordToCompare.contains(actualWord)) {
                        substrings.add(actualWord);
                    }
                }
            }
        }
        return new ArrayList<>(substrings);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.stringMatching(new String[]{"leetcoder","leetcode","od","hamlet","am"}).toString());
    }
}