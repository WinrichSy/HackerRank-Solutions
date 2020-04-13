//Plus Minus
//https://www.hackerrank.com/challenges/plus-minus/problem

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

    // Complete the plusMinus function below.
    static void plusMinus(int[] arr) {
        float negatives = 0;
        float positives = 0;
        float zeroes = 0;

        for(int i=0; i<arr.Length; i++)
        {
            if(arr[i] < 0)
            {
                negatives++;
            }
            else if(arr[i] > 0)
            {
                positives++;
            }
            else if(arr[i] == 0)
            {
                zeroes++;
            }

        }

        System.Console.WriteLine(positives/arr.Length);
        System.Console.WriteLine(negatives/arr.Length);
        System.Console.WriteLine(zeroes/arr.Length);

    }

    static void Main(string[] args) {
        int n = Convert.ToInt32(Console.ReadLine());

        int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp))
        ;
        plusMinus(arr);
    }
}
