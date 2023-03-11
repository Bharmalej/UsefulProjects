# Script for download some videos from Youtube by pytube library

import pytube

links = [
# 'https://www.youtube.com/watch?v=xhMvuiQNaag',
    # 'https://www.youtube.com/watch?v=BLRr-Qyp8-0',
    # 'https://www.youtube.com/watch?v=hQZCaRf6rcc',
    # 'https://www.youtube.com/watch?v=LFNj7YICkYI',
    # 'https://www.youtube.com/watch?v=h3UfhOZdtc0',
    # 'https://www.youtube.com/watch?v=CWC2fc63FmU',
    # 'https://www.youtube.com/watch?v=-2jNmKG96eo',
    # 'https://www.youtube.com/watch?v=n8X4ELvpuOQ',
    # 'https://www.youtube.com/watch?v=G8jpp-cXw9Q',
    'https://www.youtube.com/watch?v=2uGDwkcwhfo',
    'https://www.youtube.com/watch?v=6SrbKFl1N5k',
    'https://www.youtube.com/watch?v=9mLln1nQrnw',
    'https://www.youtube.com/watch?v=0RgSD-9Tkk8',
    'https://www.youtube.com/watch?v=9M_bKohJVAI',
    'https://www.youtube.com/watch?v=Zs0Y4nkhvH0',
    'https://www.youtube.com/watch?v=JabpbI_iXUM',
    'https://www.youtube.com/watch?v=ho_lZ3XfJoE'
    ]

for link in links:
    yt = pytube.YouTube(link)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    print(f'Downloading {stream.title}...')
    stream.download('/Users/ke/Downloads/workouts')
    print(f'Downloaded {stream.title}.')