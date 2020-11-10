import sys
import re


class Matrix:

    def _init_(self,rows,columns,name):
        self.rows = rows
        self.columns = columns
        self.name = name
        self.matrix = []

    
    
    
    def add_val(self,val):
        self.matrix.append(val)

    def size(self):
        print(self.rows,"x",self.columns)
        

    def is_row(self):
        if self.rows == 1:
            print("yes")
            return True
        else:
            print("no")
            return False 

    def is_column(self):
        if self.columns == 1:
            print("yes")
            return True
        else:
            print("no")
            return False

    def is_rectangular(self):
        if self.rows != self.columns:
            print("yes")
            return True
        else:
            print("no")
            return False
    
    def is_square(self):
        if self.rows == self.columns:
            print("yes")
            return True
        else:
            print("no")
            return False

    def is_diagonal(self):
        if self.rows == self.columns:
            for i in range(len(self.matrix)):
                if i > 0 and i <= self.columns:
                    if self.matrix[i] != 0:
                        print("no")
                        return False
                elif i > self.columns and i%(self.columns+1) != 0:
                    if self.matrix[i] != 0:
                        print("no")
                        return False
            print("yes")
            return True
        else:
            print("no")
            return False

    def is_scalar(self):
        if self.rows == self.columns:
            for i in range(len(self.matrix)):
                if i > 0 and i <= self.columns:
                    if self.matrix[i] != 0:
                        print("no")
                        return False
                elif i > self.columns and i%(self.columns+1) != 0:
                    if self.matrix[i] != 0:
                        print("no")
                        return False
            if self.matrix[0] == 0:
                print("no")
                return False
            else:
                const = self.matrix[0]
            for i in range(len(self.matrix)):
                if i > self.columns:
                    if i%(self.columns+1) == 0:
                        if self.matrix[i] != const:
                            print("no")
                            return False
            print("yes")
            return True
        else:
            print("no")
            return False

    def is_identity(self):
        if self.rows == self.columns:
            for i in range(len(self.matrix)):
                if i > 0 and i <= self.columns:
                    if self.matrix[i] != 0:
                        print("no")
                        return False
                elif i > self.columns and i%(self.columns+1) != 0:
                    if self.matrix[i] != 0:
                        print("no")
                        return False
            if self.matrix[0] != 1:
                print("no")
                return False
            for i in range(len(self.matrix)):
                if i > self.columns:
                    if i%(self.columns+1) == 0:
                        if self.matrix[i] != 1:
                            print("no")
                            return False
            print("yes")
            return True
        else:
            print("no")
            return False    

    def is_upper_triangular(self):
        if self.rows == self.columns:
            for i in range(self.rows-1):
                for j in range(i+1):
                    if self.matrix[(i+1)*self.rows+j] != 0:
                        print("no")
                        return False
            print("yes")
            return True
        else:
            print("no") 
            return False

    def is_lower_triangular(self):
        if self.rows == self.columns:
            for i in range(self.rows-1):
                for j in range(self.rows-(i+1)):
                    if self.matrix[i*self.rows+j+(1+i)] != 0:
                        print("no")
                        return False
            print("yes")
            return True
        else:
            print("no") 
            return False

    def is_null(self):
        for i in range(len(self.matrix)):
            if self.matrix[i] != 0:
                print("no")
                return False
        print("yes")
        return True

    def is_symmetric(self):
        if self.rows == self.columns:
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.matrix[self.columns*i+j] != self.matrix[self.columns*j+i]:
                        print("no")
                        return False
            print("yes")
            return True
        else:
            print("no")
            return False

    def is_skew_symmetric(self):
        if self.rows == self.columns:
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.matrix[self.columns*i+j] + self.matrix[self.columns*j+i] != 0:
                        print("no")
                        return False
            print("yes")
            return True
        else:
            print("no")
            return False

    def are_equal(self,m2):
        if self.rows == m2.rows and self.columns == m2.columns:
            for i in range(len(self.matrix)):
                if self.matrix[i] != m2.matrix[i]:
                    print("no") 
                    return False
            print("yes")
            return True   
        else:
            print("no")
            return False

    def _add_(self,m2):
        if self.rows == m2.rows and self.columns == m2.columns:
            res_name = None
            result = Matrix()
            result._init_(self.rows,self.columns,res_name)
            for i in range(len(self.matrix)):
                result.add_val(self.matrix[i] + m2.matrix[i])
            print("ans =")
            for i in range(result.rows):
                    for j in range(result.columns):
                        print(result.matrix[result.columns*i+j], " ", end=" ")
                    print("\n")
            return result
        else:
            print("Error: matricies are not of same size")
            return self

    def _sub_(self,m2):
        if self.rows == m2.rows and self.columns == m2.columns:
            res_name = None
            result = Matrix()
            result._init_(self.rows,self.columns,res_name)
            for i in range(len(self.matrix)):
                result.add_val(self.matrix[i] - m2.matrix[i])
            print("ans =")
            for i in range(result.rows):
                    for j in range(result.columns):
                        print(result.matrix[result.columns*i+j], " ", end=" ")
                    print("\n")
            return result
        else:
            print("Error: matricies are not of same size")
            return self

    def _mul_(self,m2):
        if self.columns == m2.rows:
            res_name = None
            result = Matrix()
            result._init_(self.rows,m2.columns,res_name)
            for i in range(self.rows):
                for j in range(m2.columns):
                    val = 0
                    for k in range(self.columns):
                        val +=self.matrix[self.columns*i+k] * m2.matrix[m2.columns*k+j]
                    result.add_val(val)
            print("ans =")
            for i in range(result.rows):
                    for j in range(result.columns):
                        print(result.matrix[result.columns*i+j], " ", end=" ")
                    print("\n")
            return result
        else:
            print("Error: column and row sizes !=")
            return self

    def _invert_(self):
        if self.rows == self.columns:
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.columns*i+j < len(self.matrix)/2:
                        temp = self.matrix[self.columns*i+j]
                        self.matrix[self.columns*i+j] = self.matrix[self.columns*j+i]
                        self.matrix[self.columns*j+i] = temp
            for i in range(self.rows):
                for j in range(self.columns):
                    print(self.matrix[self.columns*i+j], " ", end=" ")
                print("\n")
        else:
            print("Error: matrix must be square")
            return self 


def equal(strng,lst):
    for i in range(len(lst)-1):
        if lst[i].name in strng:
            for j in range(len(lst)-i-1):
                if lst[i+j+1].name in strng:
                    lst[i].are_equal(lst[i+j+1])
                    return
            print("Matrix not found")
            return
    print("Matrix not found")
    return
                

matricies = list()
if len(sys.argv) == 2:
    file1 = open(sys.argv[1],'r')
    txt = file1.readlines()
flag = 0
line = 0
while flag != 1 and line != len(txt):
    if len(sys.argv) == 2:
        s = txt[line]
    else:
        s = input("Enter command: ")
    s_lst = list(s)
    if s == 'exit':
        flag = 1
    elif '=' in s and '[' in s:
        j = 0
        rows = 0
        while s_lst[j] != '=':
            j +=1
        name = s[0:j-1]
        for i in range(len(s)):
            if s_lst[i] == ';':
                rows +=1
        if '.' in s:
            extract_nums = map(float, re.findall('\d+\.\d+', s))    
        else:
            extract_nums = map(int, re.findall('\d+', s))
        list_nums = list(extract_nums)
        columns = int(len(list_nums)/rows)
        new_matrix = Matrix()
        new_matrix._init_(rows,columns,name)
        new_matrix.matrix = list_nums    
        print(new_matrix.name, '=', '\n',)
        idx = 0
        for j in range(rows):
            for i in range(columns):
                print(list_nums[columns*j+i], " ", end=" ")
            print("\n")
        matricies.append(new_matrix)
    elif 'size' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].size()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].size()
                break 
    elif 'isRow' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_row()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_row()
                break
    elif 'isColumn' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_column()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_column()
                break
    elif 'isRectangular' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_rectangular()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_rectangular()
                break
    elif 'isSquare' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_square()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_square()
                break
    elif 'isDiagonal' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_diagonal()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_diagonal()
                break
    elif 'isScalar' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_scalar()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_scalar()
                break
    elif 'isIdentity' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_identity()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_identity()
                break 
    elif 'isUpperTriangular' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_upper_triangular()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_upper_triangular()
                break
    elif 'isLowerTriangular' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_lower_triangular()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_lower_triangular()
                break 
    elif 'isNull' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_null()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_null()
                break 
    elif 'isSymmetric' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_symmetric()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_symmetric()
                break
    elif 'isSkewSymmetric' in s:
        for i in range(len(matricies)):
            if i == len(matricies)-1:
                if matricies[i].name in s:
                    matricies[i].is_skew_symmetric()
                else:
                    print("Matrix not found")            
            elif matricies[i].name in s:
                matricies[i].is_skew_symmetric()
                break
    elif 'areEqual' in s:
        equal(s,matricies)            
    else:
        elements = re.split(' ',s)
        print(elements)
        for i in range(len(elements)):
            if elements[i] == '+':
                for j in range(len(matricies)):
                    if matricies[j].name == elements[i-1]:
                        m1 = matricies[j]
                for k in range(len(matricies)):
                    if matricies[k].name == elements[i+1]:
                        m2 = matricies[k]
                        m1._add_(m2)
            if elements[i] == '-':
                for j in range(len(matricies)):
                    if matricies[j].name == elements[i-1]:
                        m1 = matricies[j]
                for k in range(len(matricies)):
                    if matricies[k].name == elements[i+1]:
                        m2 = matricies[k]
                        m1._sub_(m2) 
            if elements[i] == '*':
                for j in range(len(matricies)):
                    if matricies[j].name == elements[i-1]:
                        m1 = matricies[j]
                for k in range(len(matricies)):
                    if matricies[k].name == elements[i+1]:
                        m2 = matricies[k]
                        m1._mul_(m2)
            if elements[i] == '~':
                for j in range(len(matricies)):
                    if matricies[j].name == elements[i-1]:
                        m1 = matricies[j]
                        m1._invert_()
                   
    if len(sys.argv) == 2:
        line +=1

