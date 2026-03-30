class Solution {
public:
    bool isDig(char s) {
        if (s == '1' || s == '2' || s == '3' || s == '4' || s == '5' ||
            s == '6' || s == '7' || s == '8' || s == '9') {
                return true;
        }
        return false;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < board.size(); i++) {
            set<char> seenNums;
            for (int j = 0; j < board.at(i).size(); j++) {
                if (board.at(i).at(j) != '.' && !isDig(board.at(i).at(j))) {
                    return false;
                }
                else if (seenNums.find(board.at(i).at(j)) != seenNums.end()) {
                    return false;
                }

                if (board.at(i).at(j) != '.') {
                    seenNums.insert(board.at(i).at(j));
                }
            }
        }

        for (int i = 0; i < 9; i++) {
            set<char> seenNums;
            for (int j = 0; j < 9; j++) {
                if (board.at(j).at(i) != '.' && !isDig(board.at(j).at(i))) {
                    return false;
                }
                else if (seenNums.find(board.at(j).at(i)) != seenNums.end()) {
                    return false;
                }

                if (board.at(j).at(i) != '.') {
                    seenNums.insert(board.at(j).at(i));
                }
            }
        }

        int startRow = 0;
        int startCol = 0;

        while (startRow <= 6 && startCol <= 6) {
            set<char> seenNums;
            for (int row = startRow; row < startRow + 3; row++) {
                for (int col = startCol; col < startCol + 3; col++) {
                    if (board.at(row).at(col) != '.' && !isDig(board.at(row).at(col))) {
                        return false;
                    }
                    else if (seenNums.find(board.at(row).at(col)) != seenNums.end()) {
                        return false;
                    }
                    if (board.at(row).at(col) != '.') {
                        seenNums.insert(board.at(row).at(col));
                    }
                }
            }
            startCol += 3;
            if (startCol > 6) {
                startRow += 3;
                startCol = 0;
            }
        }
        return true;
    }
};
