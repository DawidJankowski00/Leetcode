using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindSubtreeSizes(int[] parent, string s) {
        int n = parent.Length;

        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new List<int>();
        }
        for (int i = 1; i < n; i++) {
            adj[parent[i]].Add(i);
        }

        int[] newParent = (int[])parent.Clone();
        int[] lastSeen = new int[26];
        Array.Fill(lastSeen, -1);

        void DfsFindParents(int u) {
            int charIdx = s[u] - 'a';
            int prevAncestor = lastSeen[charIdx];

            if (prevAncestor != -1) {
                newParent[u] = prevAncestor;
            }

            lastSeen[charIdx] = u;

            foreach (int v in adj[u]) {
                DfsFindParents(v);
            }

            lastSeen[charIdx] = prevAncestor;
        }

        DfsFindParents(0);

        List<int>[] newAdj = new List<int>[n];
        for (int i = 0; i < n; i++) {
            newAdj[i] = new List<int>();
        }
        for (int i = 1; i < n; i++) {
            newAdj[newParent[i]].Add(i);
        }

        int[] answer = new int[n];

        int DfsCalcSizes(int u) {
            int size = 1;
            foreach (int v in newAdj[u]) {
                size += DfsCalcSizes(v);
            }
            answer[u] = size;
            return size;
        }

        DfsCalcSizes(0);

        return answer;
    }
}