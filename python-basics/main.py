"""Small driver that demonstrates the pipeline in `utils.py`.

This file constructs a raw sample list, runs the three-stage pipeline
(clean -> filter -> summarize) implemented in the `utils` module, and prints
the results. Treat this as a simple example or smoke test for the helpers.
"""

import utils as ut

rd = [1, 2, None, 30, 'invalid', 40, -3, 100, None, 70, 'N/A', 70, 0, 65]
print(f'Raw Data: {rd}')
print(f'Total items: {len(rd)}')

# Run the pipeline: clean_data -> filter_data -> summary_data
summary = ut.clean_data(rd)
summary = ut.filter_data(summary)
summary = ut.summary_data(summary)