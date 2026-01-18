class Solution(object):
    def is_isomorphic(self, s: str, t: str) -> bool:
        """
        Check if two strings are isomorphic using bidirectional mapping.

        Time: O(n) - single pass through strings
        Space: O(k) - two maps where k = distinct characters (effectively O(1) for fixed alphabet)
        """
        if len(s) != len(t):
            return False

        map_s_to_t: dict[str, str] = {}
        map_t_to_s: dict[str, str] = {}

        for cs, ct in zip(s, t):
            # Check s -> t mapping
            if cs in map_s_to_t:
                if map_s_to_t[cs] != ct:
                    return False
            else:
                map_s_to_t[cs] = ct

            # Check t -> s mapping (prevents collision: two s chars -> same t char)
            if ct in map_t_to_s:
                if map_t_to_s[ct] != cs:
                    return False
            else:
                map_t_to_s[ct] = cs

        return True


if __name__ == "__main__":
    for input, output in (
        (("egg", "add"), True),
        (("apple", "bbnbm"), False),
        (("paper", "title"), True),
        (("foo", "bar"), False),
        (("ab", "aa"), False),  # Collision test
    ):
        assert Solution().is_isomorphic(*input) == output
