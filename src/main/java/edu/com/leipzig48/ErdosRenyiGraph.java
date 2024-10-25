package edu.com.leipzig48;

import edu.princeton.cs.algs4.Graph;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import java.util.Random;


public class ErdosRenyiGraph {
    /**
     * Unit tests the {@code ErdosRenyiGraph} data type.
     *
     * @param args the command-line arguments
     */
    public static void main(String[] args) {
        int V = Integer.parseInt(args[0]);
        Graph graph = new Graph(V);
        for (int i = 0; i < V; i++) {
            Random rand = new Random();
  
            int rand_int1 = rand.nextInt(V);
            int rand_int2 = rand.nextInt(V);

            graph.addEdge(rand_int1, rand_int2);
        }
        StdOut.println(graph);
    }
}
