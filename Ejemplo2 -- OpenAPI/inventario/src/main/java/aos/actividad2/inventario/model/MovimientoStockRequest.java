package aos.actividad2.inventario.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class MovimientoStockRequest {
    private Long productoId;
    private Integer cantidad;
    private TipoMovimiento tipo;
    private OrigenMovimiento origen;
    private Long origenId;
}
