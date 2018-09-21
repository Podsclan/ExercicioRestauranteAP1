# ExercicioRestauranteAP1

ENUNCIADO

Considere o sistema que o cadastro e avaliação que clientes de vão a um determinado restaurante. Nesse sistema, deve permitir:  

 

-       Cadastrar um cliente com seu (nome, e-mail, avaliação e número de estrelas).  Garanta que o e-mail possua um @. Não permita cadastro com duplicidade de e-mail. O campo de avaliação será um texto escrito pelo usuário.

-       Listar as avaliações, exibindo-se primeiro as avaliações 5 estrelas, depois 4 estrelas, 3 estrelas e assim por diante.

-       Crie uma classificação automática de avaliações em positivas ou negativas. Para fazer essa classificação você deve se basear exclusivamente no texto da avaliação escrito. Procure nesse texto os termos [“bom”, “excelente”, “ótimo”] para dizer se uma avaliação é “positiva” ou os termos [“ruim”, “péssimo”, “horrível”] para classificar ao avaliação como “negativa.” Caso não tenha certeza sobre a avaliação classifique-a como “indeterminada”

-       Atualizar uma avaliação: o usuário digita o e-mail cadastrado e, caso ele esteja cadastrado, deve ser possível atualizar o texto da avaliação. Se o e-mail não estiver cadastrado o usuário pode optar por cadastrar o usuário.

-       Informar qual a nota média do restaurante (baseado no número de estrelas)
