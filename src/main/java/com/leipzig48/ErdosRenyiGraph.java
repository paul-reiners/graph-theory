package com.leipzig48;

import edu.princeton.cs.algs4.Graph;
import edu.princeton.cs.algs4.StdOut;
import java.util.Random;

/**
 * This class generates an ErdQsRényi graph, which is a random graph model
 * defined by a fixed number of vertices {@code V} and edges {@code E}.
 * The graph may contain self-loops and parallel edges.
 */
public class ErdosRenyiGraph {
    private final int V;
    private final int E;
    private final Graph graph;

    /**
     * Constructs an ErdQsRényi graph with {@code V} vertices and {@code E} edges.
     * 
     * @param V the number of vertices
     * @param E the number of edges
     * @throws IllegalArgumentException if {@code V < 1} or {@code E < 0}
     */
    public ErdosRenyiGraph(int V, int E) {
        if (V < 1) throw new IllegalArgumentException("Number of vertices must be at least 1.");
        if (E < 0) throw new IllegalArgumentException("Number of edges cannot be negative.");
        
        this.V = V;
        this.E = E;
        this.graph = new Graph(this.V);
        Random rand = new Random();

        for (int i = 0; i < this.E; i++) {
            int rand_int1 = rand.nextInt(this.V);
            int rand_int2 = rand.nextInt(this.V);
            graph.addEdge(rand_int1, rand_int2);
        }
    }

    /**
     * Returns the generated ErdQsRényi graph.
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
            StdOut.println("Usage: java ErdosRenyiGraph <vertices> <edges>");
            return;
        }

        int V = Integer.parseInt(args[0]);
        int E = Integer.parseInt(args[1]);

        ErdosRenyiGraph erGraph = new ErdosRenyiGraph(V, E);
        StdOut.println(erGraph);
    }
}
