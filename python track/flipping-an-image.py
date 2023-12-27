class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            l,r=0, len(img)-1
            while l<r:
                img[l],img[r]=img[r],img[l]
                l+=1
                r-=1
        for img in image:
            for j in range(len(img)):
                if img[j]==1:
                    img[j]=0
                else:
                    img[j]=1
        return image


                