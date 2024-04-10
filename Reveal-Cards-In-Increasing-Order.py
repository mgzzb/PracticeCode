'''
Runtime: 44 ms
Memory: 16.84 MB
'''


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck = sorted(deck)
        deck.reverse()  # deck = [::-1]

        size = len(deck)
        final = [0] * size

        idx_deck = 0
        idx_final = 0

        skip = False

        # Repeat while cards available
        while idx_deck < size:
            if final[idx_final] == 0:

                if not skip:
                    # Top card revealed
                    final[idx_final] = deck.pop()
                    idx_deck += 1

                # Next card moved to bottom
                skip = not skip

            # add 1 to idx_final and make sure it stays within the size of array
            idx_final = (idx_final + 1) % size
        
        # return order of the deck in increasing order
        return final
