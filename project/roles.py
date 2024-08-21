from rolepermissions.roles import AbstractUserRole

class Orientador(AbstractUserRole):
    available_permissions = {
        'visualizar_comentario': True,
        'listar_comentario': True,
        
        'listar_agenda': True,
        'visualizar_agenda': True,
        'editar_agenda': True,
        'editar_agenda_status': True,

        'listar_todos_planos_estudos': True,
        'listar_plano_estudo': True,
        'visualizar_plano_estudo': True,
        'criar_plano_estudo': True,
        'editar_plano_estudo': True,
        'excluir_plano_estudo': True,

        'listar_turma': True,
        'visualizar_turma': True,
        'criar_turma': True,
        'editar_turma': True,
        'excluir_turma': True,
    } 


class Aluno(AbstractUserRole):
    available_permissions = {
        'listar_comentario': True,
        'visualizar_comentario': True,
        'criar_comentario': True,
        'editar_comentario': True,
        'excluir_comentario': True,

        'listar_agenda': True,
        'visualizar_agenda': True,
        'criar_agenda': True,
        'editar_agenda': True,
        'excluir_agenda': True,

        'listar_todos_planos_estudos': True,
        'listar_plano_estudo': True,
        'visualizar_plano_estudo': True,

        'listar_turma': True,
        'visualizar_turma': True,
    }
