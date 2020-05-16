public class Solution {

    public String addStrings(String num1, String num2) {
        String restOfValues = "";
        int lengthDifference = num1.length() - num2.length();

        if (lengthDifference > 0) {
            restOfValues = num1.substring(0, lengthDifference);
            num1 = num1.substring(lengthDifference);
        } else if (lengthDifference < 0) {
            restOfValues = num2.substring(0, -lengthDifference);
            num2 = num2.substring(-lengthDifference);
        }
        StringBuilder sumBuilder = new StringBuilder();

        int overflow = 0;

        for (int i = num1.length() - 1; i >= 0; i--) {
            int sum = overflow + (num1.charAt(i) + num2.charAt(i) - 96);

            if (sum >= 10) {
                int rest = sum % 10;
                overflow = sum / 10;
                sumBuilder.append(rest);
            } else {
                overflow = 0;
                sumBuilder.append(sum);
            }
        }

        for (int i = restOfValues.length() - 1; i >= 0; i--) {
            int sum = overflow + (restOfValues.charAt(i) - 48);

            if (sum >= 10) {
                int rest = sum % 10;
                overflow = sum / 10;
                sumBuilder.append(rest);
            } else {
                overflow = 0;
                sumBuilder.append(sum);
            }
        }

        if (overflow > 0) {
            sumBuilder.append(overflow);
        }

        return sumBuilder.reverse().toString();
    }
}