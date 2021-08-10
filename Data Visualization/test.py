

import os
for i in range(1,51):
    with open(f'example_{i}.py','a') as f:
        if os.path.isfile('f'):
            os.remove()
        else:
            with open(f'example_{i}.py','a') as z:
                z.write('#')

print('done')