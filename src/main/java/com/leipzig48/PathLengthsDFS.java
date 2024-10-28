package com.leipzig48;

import java.util.Random;
import java.util.stream.StreamSupport;

import edu.princeton.cs.algs4.DepthFirstPaths;
import edu.princeton.cs.algs4.Graph;

public class PathLengthsDFS {
    public static void main(String[] args) {
        Random rand = new Random();
        for (int v = 1; v < 256; v++) {
            System.out.println("v: " + v);
            for (int e = 0; e < 256; e++) {
                System.out.println("\te: " + e);
                int count = 0;
                long totalLength = (long) 0;
                for (int i = 0; i < 128; i++) {
                    ErdosRenyiGraph erdosRenyiGraph = new ErdosRenyiGraph(v, e);
                    Graph graph = erdosRenyiGraph.getGraph();
                    int s = rand.nextInt(v);
                    int vertex2 = rand.nextInt(v);
        
                    DepthFirstPaths depthFirstPaths = new DepthFirstPaths(graph, s);
                    boolean found =  depthFirstPaths.hasPathTo(vertex2);
                    if (found) {
                        count++;
                        Iterable<Integer> path =  depthFirstPaths.pathTo(vertex2);
                        long length = StreamSupport.stream(path.spliterator(), false).count();
                        totalLength += length;
                    }
                }

                System.out.println("\t\tFraction: " + ((double) count / 128.0) + "; Average length: " + ((double) totalLength / 128.0));
            }
        }
    }
}
