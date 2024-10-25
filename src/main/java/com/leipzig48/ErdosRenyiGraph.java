package com.leipzig48;

import edu.princeton.cs.algs4.Graph;
import edu.princeton.cs.algs4.StdOut;
import java.util.Random;


/**
 * Takes integer values <i>V</i> and <i>E</i> from the command line and builds a
 * graph by generating <i>E</i> random pairs of integers between <i>0</i> and 
 * <i>V - 1</i>.  <i>Note:</i> This generator produces self-loops and parallel 
 * edges.
 */
public class ErdosRenyiGraph {
    private int V;
    private int E;
    private Graph graph;

    public Graph getGraph() {
        return this.graph;
    }

    public ErdosRenyiGraph(int V, int E) {
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
     * Unit tests the {@code ErdosRenyiGraph} data type.
     *
     * @param args the command-line arguments
     */
    public static void main(String[] args) {
        int V = Integer.parseInt(args[0]);
        int E = Integer.parseInt(args[1]);
        Graph graph = new Graph(V);
        for (int i = 0; i < E; i++) {
            Random rand = new Random();
  
            int rand_int1 = rand.nextInt(V);
            int rand_int2 = rand.nextInt(V);

            graph.addEdge(rand_int1, rand_int2);
        }
        StdOut.println(graph);
    }
}
