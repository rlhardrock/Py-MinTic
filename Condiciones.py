# informacion = {
# 'id_prestamo' : 'RETOS_001',
# 'casado' : 'No',
# 'dependientes' : '1',
# 'educacion' : 'Graduado',
# 'independiente' : 'Si',
# 'ingreso_deudor': 4692,
# 'ingreso_codeudor': 0,
# 'cantidad_prestamo' : 106,
# 'plazo_prestamo' : 360,
# 'historia_credito' : 1,
# 'tipo_propiedad' : 'Rural'  
# }

# informacion = {
# 'id_prestamo' : 'RETOS_002',
# 'casado' : 'No',
# 'dependientes' : '3+',
# 'educacion' : 'No Graduado',
# 'independiente' : 'No',
# 'ingreso_deudor'  : 1830,
# 'ingreso_codeudor': 0,
# 'cantidad_prestamo': 100,
# 'plazo_prestamo' : 360,
# 'historia_credito' : 0,
# 'tipo_propiedad' : 'Urbano'  
# }

# informacion = {
# 'id_prestamo' : 'RETOS_003',
# 'casado' : 'No',
# 'dependientes' : '0',
# 'educacion' : 'No Graduado',
# 'independiente' : 'No',
# 'ingreso_deudor' : 3748,
# 'ingreso_codeudor' : 1668,
# 'cantidad_prestamo' : 110,
# 'plazo_prestamo' : 360,
# 'historia_credito' : 1,
# 'tipo_propiedad' : 'Semiurbano'  
# }

# informacion = {
# 'id_prestamo' : 'RETOS_004',
# 'casado' : 'No',
# 'dependientes' : '3+',
# 'educacion' : 'Graduado',
# 'independiente' : 'No',
# 'ingreso_deudor' : 3083,
# 'ingreso_codeudor' : 0,
# 'cantidad_prestamo' : 255,
# 'p_p' : 360,
# 'historia_credito' : 1,
# 'tipo_propiedad' : 'Rural'  
# }

# informacion = {
# 'id_prestamo' : 'RETOS_005',
# 'casado' : 'Si',
# 'dependientes' : '1',
# 'educacion' : 'Graduado',
# 'independiente' : 'Si',
# 'ingreso_deudor' : 11500,
# 'ingreso_codeudor' : 0,
# 'cantidad_prestamo' : 286,
# 'p_p' : 360,
# 'historia_credito' : 0,
# 'tipo_propiedad' : 'Urbano'  
# }

informacion = {
'id_prestamo' : 'RETOS_006',
'casado' : 'No',
'dependientes' : '2',
'educacion' : 'No Graduado',
'independiente' : 'Si',
'ingreso_deudor' : 11500,
'ingreso_codeudor' : 1000,
'cantidad_prestamo' : 86,
'p_p' : 360,
'historia_credito' : 0,
'tipo_propiedad' : 'Urbano'  
}

# informacion = {
# 'id_prestamo' : 'RETOS_007',
# 'casado' : 'No',
# 'dependientes' : '0',
# 'educacion' : 'Graduado',
# 'independiente' : 'No',
# 'ingreso_deudor' : 1111,
# 'ingreso_codeudor' : 1111,
# 'cantidad_prestamo' : 90,
# 'p_p' : 360,
# 'historia_credito' : 0,
# 'tipo_propiedad' : 'Rural'  
# }

def prestamo (informacion):
    
    i_d = informacion['ingreso_deudor']
    i_c = informacion['ingreso_codeudor']
    c_p = informacion['cantidad_prestamo']
    dependientes = informacion['dependientes']
    # p_p = informacion['plazo_prestamo']
    if dependientes == '3+':
        dependientes = 3
    else:
        dependientes = int(dependientes)
    
    # Nuevo diccionario - Cliente por defecto tiene desaprobado el credito
    aprobado = {'id_prestamo' : informacion.get('id_prestamo'), 'aprobado' : False }
    #proceso de decisiones
    if informacion.get('historia_credito') == 1:
        if i_c > 0 and (i_d/9) > c_p :
            aprobado['aprobado'] = True
        else:    
            if dependientes > 2 and informacion.get('independiente') == 'Si':
                aprobado['aprobado'] = i_c/12 > c_p
            else:
                aprobado['aprobado'] = c_p < 200
    else:
        if informacion.get('independiente') == 'Si':
            if not (informacion.get('casado') == 'Si' and dependientes > 1):
                if i_d/10 > c_p or i_c/10 > c_p:
                    aprobado['aprobado'] = c_p < 180
                #else    
            #else    
        else:          
            if not (informacion.get('tipo_propiedad') == 'Semiurbano' and dependientes < 2):
                if informacion.get('educacion') == 'Graduado':
                    aprobado['aprobado'] = i_d/11 > c_p and i_c/11 > c_p
                #else    
            #else:
                         
    return aprobado

print("******************  PRUEBA   *********************")
print(prestamo(informacion))
print("****************** FIN PRUEBA  ******************")
