//2D Array - DS
//https://www.hackerrank.com/challenges/2d-array/problem

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

    // Complete the hourglassSum function below.
    static int hourglassSum(int[][] arr) {
        List<int> sums = new List<int>();
        int tempSum = 0;
        for(int i=0; i<arr.Length-2; i++)
        {
            for(int j=0; j<arr.Length-2; j++)
            {
                tempSum += arr[i][j] + arr[i][j+1] + arr[i][j+2];
                tempSum += arr[i+1][j+1];
                tempSum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
                sums.Add(tempSum);
                tempSum=0;
            }


        }

        //Check which is the highest
        int highestSum = 0;
        highestSum = sums[0];
        for(int i=0; i<sums.Count; i++)
        {
            if(sums[i] > highestSum)
            {
                highestSum = sums[i];
            }
        }

        return highestSum;

    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int[][] arr = new int[6][];

        for (int i = 0; i < 6; i++) {
            arr[i] = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp));
        }

        int result = hourglassSum(arr);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
