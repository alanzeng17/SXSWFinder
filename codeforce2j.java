import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.LinkedList;

public class codeforce2j
{
    public static class Node implements Comparable<Node> {
        int id;
        ArrayList<Edge> neighbors;
        long cost;
        LinkedList<Integer> path;
        Node parent;
        HashSet<Integer> visited;

        public Node(int id) {
            this.id = id;
            this.neighbors = new ArrayList<Edge>();
            this.cost = Long.MAX_VALUE;
            this.path = new LinkedList<Integer>();
            this.parent = null;
            this.visited = new HashSet<Integer>();
        }
        // public void setVisited(int num)
        // {
        //     visited = new boolean[num];
        // }
        public int compareTo(Node other) {
            return Long.compare(this.cost, other.cost);
        }

        public boolean nodeExist(int n)
        {
            for (int i = 0; i < neighbors.size(); i++) {
                if (n == neighbors.get(i).dest.id){
                    return true;
                }
            }
            return false;
        }
        public void modifyNode(int n, long c)
        {
            for (int i = 0; i < neighbors.size(); i++) {
                if (n == neighbors.get(i).dest.id){
                    if (c < neighbors.get(i).weight)
                        neighbors.get(i).weight = c;
                }
            }
        }
        public boolean inPath(int chkId)
        {
            for (int i = 0; i < path.size(); i++) {
                if (path.get(i) == chkId)
                    return true;
            }
            return false;
        }
        //make tostring = path format
        public String toString()
        {
            StringBuffer sb = new StringBuffer();
            for(int i = 0; i < path.size(); i++)
            {
                sb.append(path.get(i));
                sb.append(" ");
            }
            sb.append(id);
            return sb.toString();
        }

    }

    public static class Edge {
        Node dest;
        long weight;

        public Edge(Node dest, long weight) {
            this.dest = dest;
            this.weight = weight;
        }
    }
    public static void main(String args[])
    {
        Scanner in = new Scanner(System.in);
        int numNodes = in.nextInt();
        int numEdges = in.nextInt();

        Node[] arr = new Node[numNodes];
        //Create blank nodes with id = i+1
        for (int i = 0; i < numNodes; i++) {
            arr[i] = new Node(i+1);
            //arr[i].setVisited(numNodes);
        }

        //Set up adjacency list
        for (int i = 0; i < numEdges; i++) {
            int n1 = in.nextInt();
            int n2 = in.nextInt();
            long weight = in.nextLong();

            Node n = arr[n1-1];
            Node node2 = arr[n2-1];
            if (n.nodeExist(n2)) {
                n.modifyNode(n2,weight);
            }
            else {
                Edge e = new Edge(node2, weight);
                n.neighbors.add(e);
            }
            if (node2.nodeExist(n1))
                node2.modifyNode(n2, weight);
            else {
                Edge e = new Edge(n, weight);
                node2.neighbors.add(e);
            }
        }

        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        pq.add(arr[0]);
        arr[0].cost = 0;

        boolean flag = false;

        while (pq.size() != 0) {
            Node curr = pq.poll();
            if (curr.id == numNodes)
            {
                flag = true;
                System.out.println(curr.toString());
                break;
            }
            else
            {
                curr.path.add(curr.id);
                //curr.visited[curr.id-1] = true;
                curr.visited.add(curr.id);
                for (int i = 0; i < curr.neighbors.size(); i++)
                {
                    Edge e = curr.neighbors.get(i);
                    long newWeight = curr.cost + e.weight;
                    //boolean inp = curr.inPath(e.dest.id);
                    if (!curr.visited.contains(e.dest.id) && newWeight < e.dest.cost)
                    {
                        e.dest.cost = newWeight;
                        LinkedList<Integer> temp = new LinkedList<Integer>();
                        for (int x: curr.path) {
                            temp.add(x);
                        }
                        // boolean[] vtemp = new boolean[numNodes];
                        // for (int b = 0; b < numNodes; b++)
                        //     vtemp[b] = curr.visited[b];
                        // e.dest.visited = vtemp;
                        e.dest.path = temp;//may need deep copy
                        pq.add(e.dest);
                    }
                }
            }
        }

        in.close();
        if (!flag)
            System.out.println(-1);
    }
}