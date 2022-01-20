{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Binary_Search1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNDHg4o6XzIHIauGwGXFovC",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Rohith1499/coding-Design/blob/main/Binary_Search1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7vOlJIn4coBE"
      },
      "outputs": [],
      "source": [
        "#Search in a rotated sorted array:\n",
        "#time complexity : O(log n)\n",
        "#approach 1:\n",
        "\n",
        "class Solution(object):\n",
        "    def search(self, nums, target):\n",
        "        \"\"\"\n",
        "        :type nums: List[int]\n",
        "        :type target: int\n",
        "        :rtype: int\n",
        "        \"\"\"\n",
        "        l = 0\n",
        "        r = len(nums)-1\n",
        "        while l<=r:\n",
        "            mid = (l + r) // 2\n",
        "            if target == nums[mid]:\n",
        "                return mid\n",
        "            \n",
        "            if nums[l] <= nums[mid]:\n",
        "                if target > nums[mid] or target < nums[l]:\n",
        "                    l = mid + 1\n",
        "                else:\n",
        "                    r = mid - 1\n",
        "                \n",
        "            else:\n",
        "                if target < nums[mid] or target > nums[r]:\n",
        "                    r = mid - 1\n",
        "                else:\n",
        "                    l = mid + 1\n",
        "        \n",
        "        return -1\n",
        "\n",
        "#approach 2:\n",
        "\n",
        "class Solution(object):\n",
        "    def search(self, nums, target):\n",
        "        \"\"\"\n",
        "        :type nums: List[int]\n",
        "        :type target: int\n",
        "        :rtype: int\n",
        "        \"\"\"\n",
        "        l = 0\n",
        "        r = len(nums)-1\n",
        "        while l<=r:\n",
        "            mid = l + r // 2\n",
        "            if target == nums[mid]:\n",
        "                return mid\n",
        "            \n",
        "            if nums[l] <= nums[mid]:\n",
        "                if target < nums[mid] and target >= nums[l]:\n",
        "                    r = mid - 1\n",
        "                else:\n",
        "                    l = mid + 1\n",
        "                \n",
        "            else:\n",
        "                if target > nums[mid] and target <= nums[r]:\n",
        "                    l = mid + 1\n",
        "                else:\n",
        "                    r = mid - 1\n",
        "        \n",
        "        return -1"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# \"\"\"\n",
        "# This is ArrayReader's API interface.\n",
        "# You should not implement it, or speculate about its implementation\n",
        "# \"\"\"\n",
        "#class ArrayReader:\n",
        "#    def get(self, index: int) -> int:\n",
        "#time complexity : O(log n)\n",
        "class Solution:\n",
        "    def search(self, reader, target):\n",
        "        \"\"\"\n",
        "        :type reader: ArrayReader\n",
        "        :type target: int\n",
        "        :rtype: int\n",
        "        \"\"\"\n",
        "        \n",
        "        \n",
        "        end = 1\n",
        "        \n",
        "        while reader.get(end) < target:            \n",
        "            end *= 2\n",
        "            \n",
        "            \n",
        "        start = 0\n",
        "        \n",
        "        while start + 1 < end:\n",
        "            \n",
        "            mid = start + (end - start) // 2\n",
        "            \n",
        "            if reader.get(mid) == target:\n",
        "                return mid\n",
        "            elif reader.get(mid) < target:\n",
        "                start = mid\n",
        "            else:\n",
        "                end = mid\n",
        "                \n",
        "        \n",
        "        if reader.get(start) == target:\n",
        "            return start\n",
        "        \n",
        "        if reader.get(end) == target:\n",
        "            return end\n",
        "        \n",
        "        return -1"
      ],
      "metadata": {
        "id": "oed6AIYVc35S"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#time complexity : O(log n + m)\n",
        "\n",
        "class Solution(object):\n",
        "    def searchMatrix(self, matrix, target):\n",
        "        \"\"\"\n",
        "        :type matrix: List[List[int]]\n",
        "        :type target: int\n",
        "        :rtype: bool\n",
        "        \"\"\"\n",
        "        rows=len(matrix)\n",
        "        cols=len(matrix[0])\n",
        "        \n",
        "        for i in range(0,rows):\n",
        "            if(target<=matrix[i][cols-1]):\n",
        "                if(target>=matrix[i][0]):\n",
        "                    l=0\n",
        "                    r=cols-1\n",
        "                    while l <= r:\n",
        "                        m = (l + r)//2\n",
        "                        if target > matrix[i][m]:\n",
        "                            l = m + 1\n",
        "                        elif target < matrix[i][m]:\n",
        "                            r = m - 1\n",
        "                        else:\n",
        "                            return True\n",
        "                    return False\n",
        "\n",
        "#time complexity : O(log n * log m)\n",
        "\n",
        "class Solution(object):\n",
        "    def searchMatrix(self, matrix, target):\n",
        "        \"\"\"\n",
        "        :type matrix: List[List[int]]\n",
        "        :type target: int\n",
        "        :rtype: bool\n",
        "        \"\"\"\n",
        "        rows=len(matrix)\n",
        "        cols=len(matrix[0])\n",
        "        \n",
        "        top, bot = 0, rows-1\n",
        "        while top <= bot:\n",
        "            row = (top + bot)//2\n",
        "            if target > matrix[row][-1]:\n",
        "                top = row + 1\n",
        "            elif target < matrix[row][0]:\n",
        "                bot = row - 1\n",
        "            else:\n",
        "                break\n",
        "        if not(top <= bot):\n",
        "            return False\n",
        "        row = (top + bot) //2\n",
        "        l, r = 0, cols-1\n",
        "        while l <= r:\n",
        "            m = (l + r)//2\n",
        "            if target > matrix[row][m]:\n",
        "                l = m + 1\n",
        "            elif target < matrix[row][m]:\n",
        "                r = m - 1\n",
        "            else:\n",
        "                return True\n",
        "        return False"
      ],
      "metadata": {
        "id": "4-k466AaL9RS"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}