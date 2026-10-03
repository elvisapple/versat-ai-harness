Payment requires a nonempty key and positive amount. A key may be charged only once; duplicates return False. New charges return True.

Empty keys and zero or negative amounts raise `ValueError` before the charged-key
set is changed. A rejected request does not consume its key, so a corrected
positive request may succeed. Validation also applies to requests using an
already charged key. Distinct valid keys can each be charged once.
