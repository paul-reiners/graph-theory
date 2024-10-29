package com.leipzig48.graphs;

import java.util.Random;

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.Graph;

/**
 * This program takes integer values <i>V</i> and <i>E</i> from the command 
 * line and produces, with equal likelihood, each of the possible simple graphs 
 * with <i>V</i> and <i>E</i> edges.
 */
public class RandomSimpleGraph {
    private final int V;
    private final int E;
    private final Graph graph;
    private Random rand;

    private int[] getRandomPair(boolean[][] matrix) {
        int used = 0;
        for (int i = 0; i < this.V; i++) {
            for (int j = 0; j < this.V; j++) {
                if (matrix[i][j]) {
                    used++;
                }
            }
        }
        int leftOver = this.V * this.V - used;
        int randomInt = this.rand.nextInt(leftOver);
        int count = 0;
        for (int i = 0; i < this.V; i++) {
            for (int j = 0; j < this.V; j++) {
                if (i == j) {
                    continue;
                }
                if (!matrix[i][j]) {
                    if (count == randomInt) {
                        int[] result = {i, j};

                        return result;
                    } else {
                        count++;
                    }
                }
            }
        }

        return null;
    }

    /**
     * Constructs a RandomSimpleGraph with {@code V} vertices and {@code E} edges.
     * 
     * @param V the number of vertices
     * @param E the number of edges
     * @throws IllegalArgumentException if {@code V < 1} or {@code E < 0}
     */
    public RandomSimpleGraph(int V, int E) {
        if (V < 1) throw new IllegalArgumentException("Number of vertices must be at least 1.");
        if (E < 0) throw new IllegalArgumentException("Number of edges cannot be negative.");
        
        this.V = V;
        this.E = E;
        this.graph = new Graph(this.V);
        this.rand = new Random();

        boolean[][] matrix = new boolean[V][V];
        for (int i = 0; i < this.E; i++) {
            int[] pair = this.getRandomPair(matrix);
            if (pair == null) {
                throw new IllegalArgumentException("Too many edges for the number of vertices.");
            }
            int rand_int1 = pair[0];
            int rand_int2 = pair[1];
            graph.addEdge(rand_int1, rand_int2);
            matrix[rand_int1][rand_int2] = true;
            matrix[rand_int2][rand_int1] = true;
        }
    }

    /**
     * Returns the generated ErdQsRÃ©nyi graph.
     * 
     * @return the graph
     */
    public Graph getGraph() {
        return this.graph;
    }

    /**
     * Returns a string representation of the graph, showing the adjacency lists of each vertex.
     * 
     * @return a string representation of the graph
     */
    @Override
    public String toString() {
        return graph.toString();
    }

    /**
     * Unit tests the {@code ErdosRenyiGraph} data type.
     *
     * @param args the command-line arguments (first argument for vertices {@code V}, 
     *             second argument for edges {@code E})
     */
    public static void main(String[] args) {
        if (args.length < 2) {
            StdOut.println("Usage: java randomSimpleGraph <vertices> <edges>");
            return;
        }

        int V = Integer.parseInt(args[0]);
        int E = Integer.parseInt(args[1]);

        RandomSimpleGraph randomSimpleGraph = new RandomSimpleGraph(V, E);
        StdOut.println(randomSimpleGraph);
    }
}
