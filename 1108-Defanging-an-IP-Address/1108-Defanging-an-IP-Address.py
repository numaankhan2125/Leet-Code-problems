class Solution:
    def defangIPaddr(self, address: str) -> str:
        lis1=address.split(".")
        return "[.]".join(lis1)