import type { Talles} from "./Talles";
import type { Categorias } from "./Categorias";
import type { Socios } from "./Socios";

export interface Compras{
id?: number;
descripcion: string;
precio: number;
cantidad: number;
talle?:Talles;
categoria?: Categorias;
socio?:Socios;
}
