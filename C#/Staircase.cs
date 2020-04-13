//Staircase
//https://www.hackerrank.com/challenges/staircase/problem

using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution {

    // Complete the staircase function below.
    static void staircase(int n) {
        string stairs = "";

        for(int i=0; i<n; i++)
        {
            for(int j=n-i-1; j>0; j--)
            {
                stairs = stairs+" ";
            }
            for(int j=i; j>=0; j--)
            {
                stairs = stairs+"#";
            }
            if(stairs!="")
            {
                Console.WriteLine(stairs);
            }


            stairs = "";
        }

    }

    static void Main(string[] args) {
        int n = Convert.ToInt32(Console.ReadLine());

        staircase(n);
    }
}
