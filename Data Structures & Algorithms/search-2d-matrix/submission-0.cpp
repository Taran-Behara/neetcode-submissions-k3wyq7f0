class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int start = 0;
        int end = (matrix.at(0).size() * matrix.size()) - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;
            int rowIndex = mid / matrix.at(0).size();
            int colIndex = mid % matrix.at(0).size();

            int check = matrix.at(rowIndex).at(colIndex);

            if (target == check) {
                return true;
            }
            else if (target > check) {
                start = mid + 1;
            }
            else {
                end = mid - 1;
            }
        }
        return false;
    }
};
