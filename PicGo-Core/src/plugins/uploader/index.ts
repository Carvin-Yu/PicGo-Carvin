import { IPicGo, IPicGoPlugin } from '../../types'
import githubUploader from './github'

const buildInUploaders: IPicGoPlugin = () => {
  return {
    register (ctx: IPicGo) {
      githubUploader(ctx)
    }
  }
}

export default buildInUploaders
