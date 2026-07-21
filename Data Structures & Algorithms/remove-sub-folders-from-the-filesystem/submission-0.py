class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        ans = []

        for path in folder:
            if not ans or not path.startswith(ans[-1]+"/"):
                ans.append(path)

        return ans
        