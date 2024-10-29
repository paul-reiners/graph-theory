package com.leipzig48.traits;

import java.util.Random;
import java.util.stream.StreamSupport;

import com.leipzig48.graphs.ErdosRenyiGraph;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

import edu.princeton.cs.algs4.DepthFirstPaths;
import edu.princeton.cs.algs4.Graph;

public class PathLengthsDFS {
    public static void main(String[] args) {
        int upperV = Integer.parseInt(args[0]);
        int upperE = Integer.parseInt(args[1]);
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("data/out/erdos_renyi_graph/path_lengths_dfs/stats.csv", true))) {
            writer.write("V,E,fraction_connected,average_path_length");
            writer.newLine();
          
            Random rand = new Random();
            for (int v = 1; v < upperV; v++) {
                for (int e = 0; e < upperE; e += 2) {
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

                    writer.write(String.format("%d,%d,%f,%f", v, e, ((double) count / 128.0), ((double) totalLength / 128.0)));
                    writer.newLine();
                }
            }
        } catch (IOException ex) {
              ex.printStackTrace();
        }
    }
}
