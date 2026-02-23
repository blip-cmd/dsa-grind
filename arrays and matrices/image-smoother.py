class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """

        #idea
        # initialise the matrix by sizes first -> though python, try no zeros -> not possible
        # double loop to read the pixels and apply the smoother funct to it
        # smoothen function takes the image and the coordinates

        # smoothen funct:
        # get nROWS nCOLS

        # inital sum = 0
        # initial neightbours found = 0
        # two loops limited to neighbours
        # access neighbours
        # a check for bounds then increment sum
        # return sum/count

        nROWS = len(img)
        nCOLS = len(img[0])
        result = [[0 for _ in range(nCOLS) ] for _ in range(nROWS)]

        

        def smooth(img, nROWS, nCOLS, x, y):
            total, count = 0,0
            for i in range (-1,2):
                for j in range(-1,2):
                    nx,ny = x+i, y+j
                    if 0<= nx < nROWS and 0<= ny < nCOLS:
                        total += img[nx][ny]
                        count += 1

            return total//count

        for ix in range(nROWS):
            for iy in range(nCOLS):
                # print(img[ix][iy])
                result[ix][iy] = smooth(img, nROWS, nCOLS, ix, iy)

        return result