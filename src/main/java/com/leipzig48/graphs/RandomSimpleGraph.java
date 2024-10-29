package com.leipzig48.graphs;

import java.util.Random;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.Graph;

/**
 * Generates a random simple graph with exactly {@code V} vertices and {@code E} edges. 
 * This graph contains no self-loops or parallel edges.
 */
public class RandomSimpleGraph {
    private final int V;
    private final int E;
    private final Graph graph;
    private final Random rand;

    /**
     * Constructs a RandomSimpleGraph with {@code V} vertices and {@code E} edges.
     * 
     * @param V the number of vertices
     * @param E the number of edges
     * @throws IllegalArgumentException if {@code V < 1}, {@code E < 0}, or {@code E} exceeds the possible edges
     */
    public RandomSimpleGraph(int V, int E) {
        if (V < 1) throw new IllegalArgumentException("Number of vertices must be at least 1.");
        if (E < 0) throw new IllegalArgumentException("Number of edges cannot be negative.");
        if (E > V * (V - 1) / 2) {
            throw new IllegalArgumentException("Too many edges for the number of vertices without parallel edges.");
        }

        this.V = V;
        this.E = E;
        this.graph = new Graph(V);
        this.rand = new Random();
        boolean[][] matrix = new boolean[V][V];

        for (int i = 0; i < E; i++) {
            int[] pair = getRandomPair(matrix);
            int vertex1 = pair[0];
            int vertex2 = pair[1];
            graph.addEdge(vertex1, vertex2);
            matrix[vertex1][vertex2] = true;
            matrix[vertex2][vertex1] = true;
        }
    }

    /**
     * Returns an unused pair of vertices for adding an edge.
     * 
     * @param matrix adjacency matrix indicating existing edges
     * @return an array of two integers representing a valid edge pair
     */
    private int[] getRandomPair(boolean[][] matrix) {
        int count = 0;
        int randomEdgeIndex = rand.nextInt(V * (V - 1) / 2 - E);
        
        for (int i = 0; i < V; i++) {
            for (int j = i + 1; j < V; j++) {
                if (!matrix[i][j]) {
                    if (count == randomEdgeIndex) return new int[] {i, j};
                    count++;
                }
            }
        }
        throw new IllegalStateException("No valid edge pair found.");
    }

    /**
     * Returns the generated graph.
     * 
     * @return the graph
     */
    public Graph getGraph() {
        return graph;
    }

    /**
     * Returns a string representation of the graph's adjacency lists.
     * 
     * @return a string representation of the graph
     */
    @Override
    public String toString() {
        return graph.toString();
    }

    /**
     * Unit tests the {@code RandomSimpleGraph} data type.
     *
     * @param args the command-line arguments: vertices (V) and edges (E)
     */
    public static void main(String[] args) {
        if (args.length < 2) {
            StdOut.println("Usage: java RandomSimpleGraph <vertices> <edges>");
            return;
        }

        try {
            int V = Integer.parseInt(args[0]);
            int E = Integer.parseInt(args[1]);
            RandomSimpleGraph randomSimpleGraph = new RandomSimpleGraph(V, E);
            StdOut.println(randomSimpleGraph);
        } catch (NumberFormatException e) {
            StdOut.println("Both <vertices> and <edges> should be integers.");
        } catch (IllegalArgumentException e) {
            StdOut.println("Error: " + e.getMessage());
        }
    }
}
