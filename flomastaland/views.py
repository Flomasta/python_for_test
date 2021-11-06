from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    a = 'Finally here is the first page with Python!'

    text = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. A consequatur eligendi itaque minima nihil non, officiis
    perspiciatis provident repellat temporibus. At doloribus incidunt itaque modi repellendus, sint sit vel velit?
   
    Atque culpa esse explicabo laboriosam repellendus tenetur voluptatem? Asperiores consequuntur culpa distinctio,
    magnam molestiae neque repellat reprehenderit! Accusantium atque cum enim et explicabo id impedit minus officia?
    Illo, nisi, quasi!
    
    Aspernatur cum dignissimos earum eligendi, esse inventore labore minima molestiae perferendis quaerat quasi quidem
    quis rerum saepe tempore totam ut veritatis. Autem eos labore, laboriosam necessitatibus nostrum quo ratione sunt.
    
    <Accusantium dolorem eaque earum facilis iure nemo quibusdam rerum soluta? Accusantium corporis dolor esse nam
    necessitatibus neque officiis omnis possimus quaerat, quo rerum vitae voluptas voluptatum? Ad dolor, voluptas!
    Temporibus.
    
    Assumenda corporis distinctio dolorem error excepturi expedita fugit harum in, magnam nobis odit omnis optio
    placeat quae quidem, reprehenderit sed tenetur ullam voluptate voluptates. Aliquam consectetur enim nam quis
    veritatis.
    '''
    return render(request, './index.html', {
        'a': a,
        'text': text,
    })
