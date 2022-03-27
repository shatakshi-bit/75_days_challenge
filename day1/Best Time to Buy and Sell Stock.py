class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        m_p=float('inf')
        for i in range(len(prices)):
            if prices[i]<m_p:
                m_p=prices[i]
            elif prices[i]-m_p>m:
                m=prices[i]-m_p
        return m