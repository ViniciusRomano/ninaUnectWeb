def usuario_desktop(request):
    """
    Retorna True se o usuario do request esta no grupo Desktop,
    Falso caso contrario
    TODO: corrigir erro quando usuario nao tem grupo
    """
    user = request.user
    if user.groups.all()[0].name == 'desktop':
        return True
    return False