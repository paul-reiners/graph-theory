package com.leipzig48;

import org.apache.commons.lang3.tuple.Pair;

public class Main {
    public static void main(String[] args) {
        Pair<Integer, Integer> pair = Pair.of(1, 2);
        int first = pair.getLeft();
        int second = pair.getRight();

        System.out.println("First: " + first + ", Second: " + second);
    }
}
