class Solution {
    public int maxArea(int[] heights) {
        int max_area=0;
        int min_height=heights[0];
        int l = 0;
        int r = heights.length -1;
        while (l < r)
        {
            int curr_area=Math.min(heights[l],heights[r]) * (r-l);
            max_area = Math.max(max_area, curr_area);
            
            if (heights[l] < heights[r])
            {
                l++;
            }
            else
            { 
                r--;

            }
        }
        return max_area;
        }
    }
