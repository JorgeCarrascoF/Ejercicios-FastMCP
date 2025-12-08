package aos.actividad2.inventario.dto;

import aos.actividad2.inventario.model.MovimientoStock;
import java.time.LocalDateTime;

public record MovimientoStockDTO(
  Long id,
  Long productoId,
  Integer cantidad,
  TipoMovimientoDTO tipo,
  OrigenMovimientoDTO origen,
  Long origenId,
  LocalDateTime fechaMovimiento
) {
  public enum OrigenMovimientoDTO {
    CLIENTE,
    PROVEEDOR,
    INTERNO,
  }

  public enum TipoMovimientoDTO {
    ENTRADA,
    SALIDA,
  }

  public static MovimientoStockDTO fromEntity(MovimientoStock movimiento) {
    return new MovimientoStockDTO(
      movimiento.getId(),
      movimiento.getProducto().getId(),
      movimiento.getCantidad(),
      MovimientoStockDTO.TipoMovimientoDTO.valueOf(movimiento.getTipo().name()),
      MovimientoStockDTO.OrigenMovimientoDTO.valueOf(
        movimiento.getOrigen().name()
      ),
      movimiento.getOrigenId(),
      movimiento.getFechaMovimiento()
    );
  }
}
